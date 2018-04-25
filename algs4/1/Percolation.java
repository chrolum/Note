//import edu.princeton.cs.algs4.StdRandom;
//import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;


public class Percolation {
    private int n;
    private WeightedQuickUnionUF uf;
    private int virtualBegin = 0;
    private int virtualEnd = 1;
    private int beginIdx = 2;
    private boolean[] openSite; //a nxn array record status of openning without vitual point;
    // private int count = 0;//record the num of opensite
    // private []id;
    public Percolation(int n) {
        //create nxn grid, with all sites blocked
        //The row and col idx are integers between 2 and n+1, 0 mean the vitual point for the row1 , 1 mean the virtual point for the end row
        if (n <= 0) {
            throw new IllegalArgumentException("n is invalid");
        }
        this.n = n;
        uf = new WeightedQuickUnionUF(n*n + 2);
        for (int i=2; i <= n+2; i++) {
            uf.union(virtualBegin, i);
            uf.union(virtualEnd, n*(n-1)+i);      
        }
        openSite = new boolean[n*n + 2];//to duiqi
        for (int i=0; i<openSite.length; i++) {
            openSite[i] = false;
        }
    }

    public void open(int row, int col) {
        //open site (row, col), if it's not open already,while open a new side, it is time to check out weather open a new connection
        //check the new opensite up down right left
        if (row<1 || col<1) {
            throw new IllegalArgumentException("row or col is invaild");
        } 
        int idx = rcToIdxOfUf(row, col);
        if (! this.isOpen(row, col)) {
            openSite[idx] = true;
            if (row > 0 && openSite[idx]) {
                //up
                uf.union(idx, idx-n);
            }
            if (row < n && openSite[idx]) {
                //down
                uf.union(idx, idx+n);
            }
            if (col > 0 && openSite[idx]) {
                uf.union(idx, idx+1);
            }
            if (col < n && openSite[idx]) {
                uf.union(idx, idx-1);
            }
        }
        else {
            
        }
        
    }

    public boolean isOpen(int row, int col) {
        if (row<1 || col<1) {
            throw new IllegalArgumentException("row or col is invaild");
        } 
        return openSite[rcToIdxOfUf(row, col)];
    }

    public boolean isFull(int row, int col) {
        if (row<1 || col<1) {
            throw new IllegalArgumentException("row or col is invaild");
        } 
        int idx = rcToIdxOfUf(row, col);
        return uf.connected(idx, virtualBegin);

    }

    public int numberOfOpenSite() {
        int count = 0;
        for (int i=0; i<openSite.length; i++) {
            if (openSite[i] == true) {
                count++;
            }
        }
        return count;
    }

    public boolean percolates() {
        return uf.connected(virtualBegin, virtualEnd);
    }

    public static void main(String[] args) {
    
    }

    private int rcToIdxOfUf(int row, int col) {
        return (row-1)*n + col + beginIdx;
    }
}    