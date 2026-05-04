# ZDI-15-439: GE MDS PulseNET FileDownloadServlet Directory Traversal Information Disclosure And Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-439
- **ZDI-CAN:** ZDI-CAN-2906
- **Date:** 2015-09-16
- **CVE:** CVE-2015-6459
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:C
- **Affected Vendors:** GE
- **Affected Products:** MDS PulseNET
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-439/
## Vulnerability Details

This vulnerability allows remote attackers to read and delete arbitrary files on vulnerable installations of GE MDS PulseNET. Authentication is not required to exploit this vulnerability. The specific flaw exists within the FileDownloadServlet. By specifying a filename including directory traversal, an attacker can read and then delete an arbitrary file on the system. The read and subsequent deletion will be performed under the context of SYSTEM.

## Additional Details

GE has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-258-03

## Disclosure Timeline

- 2015-04-30 - Vulnerability reported to vendor
- 2015-09-16 - Coordinated public release of advisory
