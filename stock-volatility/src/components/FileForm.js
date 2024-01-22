import {useState} from 'react' ; 

function FileForm(){
    const [file , setFile] = useState(null) ; 
    const [volatilityData , setVolatilityData] = useState(null) 
    const [errorData , setErrorData] = useState(null)


    const handleFileInputChange = (event) => {
        console.log(event.target.files)
        setFile(event.target.files[0])
    }

    const handleSubmit = async (event) => {
        event.preventDefault() ; 

        const formData = new FormData();
        formData.append('fileUploaded' , file) ; 

        try{
            const endpoint = "http://localhost:8000/uploadfile/"
            const response = await fetch(endpoint , {
                method : "POST" , 
                body : formData
            });


            if(response.ok){
                console.log("File Uploaded Successfulyy!") ; 
                const result = await response.json(); 
                setVolatilityData(result);
                setErrorData(null);
            }
            else{
                setVolatilityData(null);
                const errorResponse = await response.json();
                setErrorData(errorResponse);
                console.error("Failed to upload file") ; 
            }
        }catch(error){
            console.log(error) ; 
        }

        
    }

    return (
        <div>
            <h1>Upload File</h1>
            <h3>Supported files are .csv and .xlsx</h3>

            <form onSubmit={handleSubmit}>
                <div style = {{marginBottom : "20px"}}>
                    <input type = "file" onChange={handleFileInputChange}/>
                </div>
                <button type="submit">Upload</button>
            </form>

            {file && <p>{file.name}</p>}

            {volatilityData && (
                <div>
                <p>Daily Volatility: {volatilityData.daily_volatility}</p>
                <p>Annualized Volatility: {volatilityData.annualized_volatility}</p>
                </div>
            )}

            {errorData && (
                <div>
                <p>Error Detail: {errorData.detail}</p>
                </div>
            )}

        </div>
    )
}

export default FileForm;