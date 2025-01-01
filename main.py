from PIL import Image
import numpy as np
import os
def main():
    path_cathedral = "SingularValueDecompression\images\cathedral.ppm"
    path_fireworks = "SingularValueDecompression\images\\fireworks.ppm"
    file_size_bytes_cathedral_original = os.path.getsize(path_cathedral)
    file_size_bytes_fireworks_original = os.path.getsize(path_fireworks)
    output_folder = "SingularValueDecompression\output"
    k = 500 
    print("-----cathedral.ppm-----")
    while(k >=10):
        img_uncompressed = Image.open(path_cathedral)
        img_compressed = grayscaleCompression(img_uncompressed,k)
        img_uncompressed = img_uncompressed.convert("L")
        psnr_value = calculate_psnr(img_uncompressed, img_compressed)

        # Saving file to output
        outFileNameCompressed = "cathedral_" + str(k) + ".png"
        output_path = os.path.join(output_folder, outFileNameCompressed)
        # save to folder
        img_compressed = img_compressed.convert("L")
        img_compressed.save(output_path,format='PNG')
        # calculate difference in compression
        file_size_bytes_compressed = os.path.getsize(output_path)
        file_size_difference = file_size_bytes_cathedral_original - file_size_bytes_compressed
        file_size_mb = file_size_bytes_compressed / (1024 * 1024)  
        print(f"PSNR for k={k}: {psnr_value} dB, size of file = {file_size_mb} mb")
        # Decrease k (assuming you want to reduce k in each iteration)
        k -= 10
    k = 500 # reset k value
    print("-----fireworks.ppm-----")
    while(k >=10):
        img_uncompressed = Image.open(path_fireworks)
        img_compressed = grayscaleCompression(img_uncompressed,k)
        img_uncompressed = img_uncompressed.convert("L")
        psnr_value = calculate_psnr(img_uncompressed, img_compressed)
        # Saving file to output
        outFileNameCompressed = "fireworks_" + str(k) + ".png"
        output_path = os.path.join(output_folder, outFileNameCompressed)
        # save to folder
        img_compressed = img_compressed.convert("L")
        img_compressed.save(output_path,format='PNG')
        # calculate difference in compression
        file_size_bytes_compressed = os.path.getsize(output_path)
        file_size_mb = file_size_bytes_compressed / (1024 * 1024)  
        print(f"PSNR for k={k}: {psnr_value} dB, size of file = {file_size_mb} mb")
        # Decrease k (assuming you want to reduce k in each iteration)
        k -= 10
            

def grayscaleCompression(img, k):   
        grayscale_img = img.convert("L") # representing our img as grayscale, so that there are only 2 dimensions
        A = np.array(grayscale_img) # representing our grayscale image as an array 'A'
        U,S,Vt =  np.linalg.svd(A,full_matrices=False)
        # Compress by keeping only the top k singular values
        
        S_k = np.diag(S[:k])  # Create a smaller diagonal matrix
        U_k = U[:, :k]  # Truncate U
        Vt_k = Vt[:k, :]  # Truncate V^T
        A_compressed = np.matmul(U_k, np.matmul(S_k, Vt_k))
        SVD_S = np.clip(A_compressed, 0, 255)  # Ensure values are in the range [0, 255]
        img_compressed = Image.fromarray(SVD_S)
        return img_compressed
def calculate_psnr(original, compressed):
        # Convert images to numpy arrays for calculation
        original = np.array(original, dtype=np.float64)
        compressed = np.array(compressed, dtype=np.float64)
    
        # Compute MSE (Mean Squared Error)
        mse = np.mean((original - compressed) ** 2)
    
        # To avoid division by zero, we check if MSE is 0
        if mse == 0:
            return float('inf')  # No error, identical images
    
        # Compute PSNR
        max_pixel = 255  # Maximum pixel value for 8-bit images
        psnr = 10 * np.log10((max_pixel ** 2) / mse)
        return psnr
main()

    