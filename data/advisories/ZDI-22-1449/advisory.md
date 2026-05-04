# ZDI-22-1449: Advantech R-SeeNet out.php Directory Traversal Arbitrary File Read and Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1449
- **ZDI-CAN:** ZDI-CAN-17391
- **Date:** 2022-10-21
- **CVE:** CVE-2022-3387
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** R-SeeNet
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1449/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information and delete arbitrary files on affected installations of Advantech R-SeeNet. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the filename and path parameters provided to the out.php endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information and delete files in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-291-01

## Disclosure Timeline

- 2022-06-06 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
