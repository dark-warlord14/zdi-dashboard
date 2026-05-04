# ZDI-20-343: IBM Spectrum Protect Plus cleanupUpdateImage Arbitrary Directory Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-343
- **ZDI-CAN:** ZDI-CAN-9949
- **Date:** 2020-03-31
- **CVE:** CVE-2020-4214
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** IBM
- **Affected Products:** Spectrum Protect Plus
- **Credit:** KPC of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-343/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary directories on affected installations of IBM Spectrum Protect Plus. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Administrative Console Framework service. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete directories in the context of root.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www.ibm.com/support/pages/node/6114130

## Disclosure Timeline

- 2019-12-12 - Vulnerability reported to vendor
- 2020-03-31 - Coordinated public release of advisory
