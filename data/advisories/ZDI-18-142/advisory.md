# ZDI-18-142: Advantech WebAccess Node certUpdate filename Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-142
- **ZDI-CAN:** ZDI-CAN-5492
- **Date:** 2018-02-06
- **CVE:** CVE-2018-5445
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess Node
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-142/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the filename parameter of certUpdate.asp. The issue results from the lack of proper validation of user-supplied data, which can allow for the upload of arbitrary files. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-023-01

## Disclosure Timeline

- 2017-12-19 - Vulnerability reported to vendor
- 2018-02-06 - Coordinated public release of advisory
- 2018-02-09 - Advisory Updated
