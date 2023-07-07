# Rotate PDF Endpoint

This API endpoint allows you to rotate a specific page of a PDF file. It uses the PyPDF2 library to perform the rotation.

## API Endpoint

### Endpoint URL

```
POST /rotate_pdf
```

### Request Parameters

- `details`: An object containing the rotation details.
  - `page` (integer): The page number to rotate.
  - `degree` (integer): The rotation angle in degrees.

- `file`: The PDF file to rotate.

### Response

The API response will include the following:

- `response` (string): A message indicating whether the PDF rotation was successful.

- `path` (string): The path of the rotated PDF file.

### Implementation Steps

1. Read the input rotation details and the PDF file.

2. Use the PyPDF2 library to open the PDF file.

3. Create a new PDF writer object.

4. Get the specified page from the PDF.

5. Rotate the page using the `rotateClockwise` method and the specified rotation degree.

6. Add the rotated page to the PDF writer.

7. Write the output PDF file using the PDF writer.

8. Close the output file.

9. Return the API response with the message indicating the success of the rotation and the path of the rotated PDF file.

That's it! With these implementation steps, you can rotate a specific page of a PDF file using this API endpoint.