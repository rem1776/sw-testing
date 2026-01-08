program hello_world
      use mpi
      implicit none

      integer :: ierror, npes, pe

      call mpi_init(ierror)
      call mpi_comm_size(mpi_comm_world, npes, ierror)
      call mpi_comm_rank(mpi_comm_world, pe, ierror)

      print *, "hello from processor", pe, "of", npes
      call mpi_finalize(ierror)
end program

