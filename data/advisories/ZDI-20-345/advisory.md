# ZDI-20-345: IBM Spectrum Protect Plus uploadHttpsCertificate Directory Traversal File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-345
- **ZDI-CAN:** ZDI-CAN-9952
- **Date:** 2020-03-31
- **CVE:** CVE-2020-4209
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:L
- **Affected Vendors:** IBM
- **Affected Products:** Spectrum Protect Plus
- **Credit:** KPC of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-345/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of IBM Spectrum Protect Plus. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the Administrative Console Framework service. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create files in the context of an administrator.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www.ibm.com/support/pages/node/6116488

## Disclosure Timeline

- 2019-12-12 - Vulnerability reported to vendor
- 2020-03-31 - Coordinated public release of advisory
