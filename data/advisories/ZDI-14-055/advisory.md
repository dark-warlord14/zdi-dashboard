# ZDI-14-055: Novell ZENworks Configuration Management PreBoot Service Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-055
- **ZDI-CAN:** ZDI-CAN-1595
- **Date:** 2014-04-03
- **CVE:** CVE-2013-3706
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:P/A:N
- **Affected Vendors:** Novell
- **Affected Products:** ZENworks Configuration Manager
- **Credit:** Mak Kolybabi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-055/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENworks Configuration Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Preboot Service (novell-pbserv.exe) which listens for incoming connections on TCP port 998. The service supports an opcode that allows for files to be downloaded through the use of directory traversal. By abusing this behavior an attacker can disclose administrative credentials and possibly leverage this situation to achieve remote code execution.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/kb/doc.php?id=7014663

## Disclosure Timeline

- 2013-01-20 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
