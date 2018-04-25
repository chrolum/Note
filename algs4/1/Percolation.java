import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class percolation {
    private int n;
    private WeightedQuickUnionUF uf
    private virtualBegin = 0;
    private virtualEnd = 1;
    private beginIdx = 2;
    private boolean[] openSite; //a nxn array record status of openning without vitual point;
    private int count = 0;//record the num of opensite
    // private []id;
    public Percolation(int n) {
        //create nxn grid, with all sites blocked
        //The row and col idx are integers between 2 and n+1, 0 mean the vitual point for the row1 , 1 mean the virtual point for the end row
        this.n = n;
        uf = new WeightedQuickUnionUF(n*n + 2)
        for (int i=2; i <= n+2; i++) {
            uf.union(virtualBegin, i);
            uf.union(vitualEnd, n*(n-1)+i);      
        }
        openSite = new boolean[(n+1)*(n+1)];
        for (int i=0; i<openSite.length; i++) {
            openSite[i] = false;
        }

    public void open(int row, int col) {
        //open site (row, col), if it's not open already,while open a new side, it is time to check out weather open a new connection
        //check the new opensite up down right left
        int idx = row*n + col
        int id = rcToIdxOfUf(row, col);
        if (! this.isOpen(row, col)) {
            openSite[row*n+col] = true;
            if (row > 0 && openSite[idx]) {
                //up
                uf.union(id, id-n);
            }
            if (row < n && openSite[idx]) {
                //down
                uf.union(id, id+n);
            }
            if (col > 0 && openSite[idx]) {
                uf.union(id, id+1);
            }
            if (col < n && openSite[idx]) {
                uf.union(id, id-1);
            }
        }
        else {
            pass;
        }
        
    }

    public boolean isOpen(int row, int col) {
        return openSite[row*n + col];
    }

    public boolean isFull(int row, int col) {
        int idx = (row-1)*n + col + beginIdx;
        return uf.connected(idx, virtualBegin);

    }

    public int numberOfOpenSite() {
        for (int i=0) {
            
        }
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