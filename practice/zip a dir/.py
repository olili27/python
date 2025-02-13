import os
from zipfile import ZipFile

# Create object of ZipFile
def zipDirectory(directory_path: str, zip_path) -> dict:
    with ZipFile(zip_path, 'w') as zip_object:
    # Traverse all files in directory
        for folder_name, sub_folders, file_names in os.walk(directory_path):
            for filename in file_names:
                # Create filepath of files in directory
                file_path = os.path.join(folder_name, filename)
                # Add files to zip file
                zip_object.write(file_path, os.path.basename(file_path))

    if os.path.exists(zip_path):
        return {"status": True, "log": "", "path": zip_path}
    
    return {"status": False, "log": "zip not created", "path": ""}


def zip_file(file_path, zip_path):
    with ZipFile(zip_path, 'w') as zipper:
        zipper.write(file_path, arcname=file_path.split("/")[-1])
    
    if os.path.exists(zip_path):
        return {"status": True, "log": "", "path": zip_path}
    
    return {"status": False, "log": "zip not created", "path": ""}

# print(zip_file("/tmp/Tier IV_Collateral Material Collateral_CMCStandard.csv", "/tmp/Tier IV_Collateral Material Collateral_CMCStandard.zip"))

from kisa_utils.storage import Path
from kisa_utils import dates

def deleteInstitutionTemplatesDirectory(directoryPath: str) -> dict:
    for _ in Path.listDirectory("/tmp/9987ML")["contents"]:
        Path.delete(_)
    return Path.delete(directoryPath)


print(Path.listDirectory("/tmp/9987ML"))