def make_pie_table(table,pat,m):	
	i=0
	j=1
	while j<m:
		if pat[i]==pat[j]:
			table[j]=i+1
			j+=1
			i+=1
		else:
			if i!=0:
				i=table[i-1]
			else:
				table[j]=0
				j+=1
	print(table)
# TAKES O(N+M) TIME AND	O(M) SPACE COMPLEXITY
def KMPSearch(pat,text):
	n,m=len(text),len(pat)
	pie_table=[0]*m
	make_pie_table(pie_table,pat,m)
	i=j=0
	while i<n:
		if text[i]==pat[j]:
			i+=1
			j+=1
		else:
			if j==0:
				i+=1
			else:
				j=pie_table[j-1]
		if j==m:
			print(f"FOUND OUR MATCHING PATTERN AT INDEX {i-j}")
			j=pie_table[j-1]#to make continue search after finding pattern
if __name__ == '__main__':
	text = "SSSSDDDABCABYsdfsddABCABY"
	pat = "ABCABY"
	KMPSearch(pat, text) 

