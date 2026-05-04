# ZDI-11-062: Multiple Vendor Calendar Manager RPC Service Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-062
- **ZDI-CAN:** ZDI-CAN-561
- **Date:** 2011-02-08
- **CVE:** CVE-2010-4435
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard, IBM, Sun Microsystems
- **Affected Products:** HP-UX AIX Solaris 10
- **Credit:** Rodrigo Rubira Branco (BSDaemon)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-062/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of the Calendar Manager RPC Service. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CMSD server (rpc.cmsd) which listens by default on UDP port 32768. The process does not properly handle large XDR-encoded ASCII strings to RPC call 10 followed by RPC call 6. This can be abused by an attacker to overflow a buffer on the remote host. Successful exploitation can result in arbitrary code execution.

## Additional Details

HP: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02702395 IBM: http://aix.software.ibm.com/aix/efixes/security/cmsd_advisory.asc IBM is not providing credits, as our system at that time and for this brand does not accept credits. Oracle: http://www.oracle.com/technetwork/topics/security/cpujan2011-194091.html

## Disclosure Timeline

- 2009-08-20 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory
