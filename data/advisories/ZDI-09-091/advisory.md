# ZDI-09-091: Hewlett-Packard Application Recovery Manager MSG_PROTOCOL Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-091
- **ZDI-CAN:** ZDI-CAN-503
- **Date:** 2009-12-08
- **CVE:** CVE-2009-3844
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Application Recovery Manager
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-091/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerability installations of HP Application Recovery Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of requests to the OmniInet process listening by default on TCP port 5555. The OmniInet process uses a custom protocol for handling requests. When handling MSG_PROTOCOL (0x010b) packets arbitrary user supplied data is copied to the stack without proper bounds checking. Successful exploitation of this vulnerability can lead to remote code execution under the SYSTEM context.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c01943909

## Disclosure Timeline

- 2009-06-25 - Vulnerability reported to vendor
- 2009-12-08 - Coordinated public release of advisory
