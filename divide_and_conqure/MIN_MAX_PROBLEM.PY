def mat_mul(mat1,mat2):
    m=len(mat1)
    n=len(mat1[0])
    p=len(mat2)
    q=len(mat2[0])

if __name__ == '__main__':
    mat1=[[1,2,3],
        [2,3,4],
        [4,5,6]]
    mat2=[[9,8,7],
        [7,6,5],
        [5,4,3]]
    print(mat_mul(mat1,mat2))