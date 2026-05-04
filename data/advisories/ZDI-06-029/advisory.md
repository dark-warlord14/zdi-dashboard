# ZDI-06-029: Ipswitch WS_FTP Server Checksum Command Parsing Buffer Overflow Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-06-029
- **ZDI-CAN:** ZDI-CAN-078
- **Date:** 2006-09-26
- **CVE:** CVE-2006-5000
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Ipswitch
- **Affected Products:** WS_FTP
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-029/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Ipswitch WS_FTP Server. Anonymous access or authentication is required to exploit this vulnerability. The specific flaw exists due to a lack of bounds checking during the parsing of long string arguments to the 'XCRC', 'XSHA1' and 'XMD5' commands leading to a stack overflow vulnerability. Exploitation requires valid or anonymous FTP server credentials.

## Additional Details

Ipswitch has issued an update to correct this vulnerability. More details can be found at: http://www.ipswitch.com/support/ws_ftp-server/releases/wr505hf1.asp

## Disclosure Timeline

- 2006-09-01 - Vulnerability reported to vendor
- 2006-09-26 - Coordinated public release of advisory
