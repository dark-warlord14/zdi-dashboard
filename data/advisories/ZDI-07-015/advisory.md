# ZDI-07-015: Novell Groupwise WebAccess Base64 Decoding Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-015
- **ZDI-CAN:** ZDI-CAN-181
- **Date:** 2007-04-18
- **CVE:** CVE-2007-2171
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** GroupWise WebAccess
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-015/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Groupwise WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists in the GWINTER.exe process bound by default on TCP ports 7205 and 7211. During the handling of an HTTP Basic authentication request, the process copies user-supplied base64 data into a fixed length stack buffer. Sending at least 336 bytes will trigger a stack based buffer overflow due to a vulnerable base64_decode() call. Exploitation of this issue can result in arbitrary code execution.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=8RF83go0nZg~

## Disclosure Timeline

- 2007-03-19 - Vulnerability reported to vendor
- 2007-04-18 - Coordinated public release of advisory
