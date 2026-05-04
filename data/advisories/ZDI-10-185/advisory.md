# ZDI-10-185: IBM TSM FastBack Server _Eventlog Format String Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-185
- **ZDI-CAN:** ZDI-CAN-657
- **Date:** 2010-09-29
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-185/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Tivoli Storage Manager Fastback. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FastBack server process (FastBackServer.exe) which listens by default on TCP port 11406. The process searches received packet data for a pipe character (0x7c) and then sends the remaining portion of the string to the event log without sanitization. By providing a specially crafted string with format specifiers this can be leveraged to trigger a format string vulnerability which can lead to arbitrary code execution in the context of the server process.

## Additional Details

http://www.ibm.com/support/docview.wss?uid=swg21443820 Issue 2

## Disclosure Timeline

- 2010-01-06 - Vulnerability reported to vendor
- 2010-09-29 - Coordinated public release of advisory
