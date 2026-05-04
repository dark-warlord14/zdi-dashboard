# ZDI-08-077: Trillian AIM IMG Tag Parsing Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-077
- **ZDI-CAN:** ZDI-CAN-408
- **Date:** 2008-12-04
- **CVE:** CVE-2008-5401
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Cerulean Studios, Cerulean Studios
- **Affected Products:** Trillian Pro 3.1
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-077/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cerulean Studios Trillian. Authentication is not required to exploit this vulnerability. The specific flaw exists within the tooltip processing code for Trillian. When creating a tooltip for an image, the application generates an XML tag including a property containing the filename. This data is then copied directly into a stack-based buffer without any length verifications which can eventually lead to code execution with the privileges of the client.

## Additional Details

Cerulean Studios has issued an update to correct this vulnerability. More details can be found at: http://blog.ceruleanstudios.com/?p=404

## Disclosure Timeline

- 2008-11-10 - Vulnerability reported to vendor
- 2008-12-04 - Coordinated public release of advisory
