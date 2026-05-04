# ZDI-16-403: Trihedral VTScada Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-403
- **ZDI-CAN:** ZDI-CAN-3513
- **Date:** 2016-07-01
- **CVE:** CVE-2016-4532
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Trihedral Engineering Ltd
- **Affected Products:** VTScada
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-403/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Trihedral VTScada. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of Wireless Application Protocol requests. The issue lies in the failure to properly restrict the path from which images are retrieved. An attacker can leverage this vulnerability to disclose the contents of arbitrary files under the context of the user running the service.

## Additional Details

Trihedral Engineering Ltd has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-159-01

## Disclosure Timeline

- 2016-02-18 - Vulnerability reported to vendor
- 2016-07-01 - Coordinated public release of advisory
