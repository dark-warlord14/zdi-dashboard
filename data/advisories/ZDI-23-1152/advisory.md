# ZDI-23-1152: RARLAB WinRAR Recovery Volume Improper Validation of Array Index Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1152
- **ZDI-CAN:** ZDI-CAN-21233
- **Date:** 2023-08-17
- **CVE:** CVE-2023-40477
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** RARLAB
- **Affected Products:** WinRAR
- **Credit:** goodbyeselene
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1152/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of RARLAB WinRAR. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of recovery volumes. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

RARLAB has issued an update to correct this vulnerability. More details can be found at: https://www.win-rar.com/singlenewsview.html?&L=0&tx_ttnews%5Btt_news%5D=232&cHash=c5bf79590657e32554c6683296a8e8aa

## Disclosure Timeline

- 2023-06-08 - Vulnerability reported to vendor
- 2023-08-17 - Coordinated public release of advisory
