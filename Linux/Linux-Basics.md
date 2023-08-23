# Linux Basic Command:

w command will show all the user corrently logged into the system:

```shell
vagrant@ubuntu2204:~$ w
 16:44:51 up 1 min,  2 users,  load average: 0.11, 0.06, 0.02
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
vagrant  pts/0    10.0.2.2         16:44   41.00s  0.02s  0.02s -bash
vagrant  pts/1    10.0.2.2         16:44    0.00s  0.02s  0.00s w
```

tee command is used to do the output and save in file togather:

```
root@ubuntu2204:~# echo "Hello World!"|tee hello-world
Hello World!
root@ubuntu2204:~# cat hello-world 
Hello World!
```