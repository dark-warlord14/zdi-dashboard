# ZDI-11-164: HP 3COM/H3C Intelligent Management Center tftpserver DATA/ERROR Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-164
- **ZDI-CAN:** ZDI-CAN-1014
- **Date:** 2011-05-10
- **CVE:** CVE-2011-1852
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** H3C Intelligent Management Center
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-164/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP 3COM/H3C Intelligent Management Center. Authentication is not required to exploit this vulnerability. The flaw exists within the tftpserver.exe component which listens by default on UDP port 69. When handling a TFTP packet type 0x03 or 0x05 (DATA or ERROR) the process blindly copies user supplied data into a fixed-length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02822750

## Disclosure Timeline

- 2010-12-01 - Vulnerability reported to vendor
- 2011-05-10 - Coordinated public release of advisory
