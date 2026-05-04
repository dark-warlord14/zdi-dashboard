# ZDI-18-546: GE MDS PulseNET FileServlet Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-546
- **ZDI-CAN:** ZDI-CAN-5520
- **Date:** 2018-06-06
- **CVE:** CVE-2018-10615
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:N/A:N
- **Affected Vendors:** GE
- **Affected Products:** MDS PulseNET
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-546/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of GE MDS PulseNET. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the FileServlet servlet. When parsing the name parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information under the context of the current service.

## Additional Details

GE has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-151-02

## Disclosure Timeline

- 2018-01-10 - Vulnerability reported to vendor
- 2018-06-06 - Coordinated public release of advisory
- 2018-06-06 - Advisory Updated
