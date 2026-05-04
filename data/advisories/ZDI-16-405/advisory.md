# ZDI-16-405: Trihedral VTScada Path Out-Of-Bounds Indexing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-405
- **ZDI-CAN:** ZDI-CAN-3575
- **Date:** 2016-07-01
- **CVE:** CVE-2016-4523
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Trihedral Engineering Ltd
- **Affected Products:** VTScada
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-405/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trihedral VTScada. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of Wireless Application Protocol requests. The issue lies in the failure to traverse user-supplied paths. An attacker can leverage this vulnerability to execute code under the context of the user running the service.

## Additional Details

Trihedral Engineering Ltd has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-159-01

## Disclosure Timeline

- 2016-02-18 - Vulnerability reported to vendor
- 2016-07-01 - Coordinated public release of advisory
