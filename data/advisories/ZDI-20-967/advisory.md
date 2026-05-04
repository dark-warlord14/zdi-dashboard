# ZDI-20-967: Marvell QConvergeConsole decryptFile Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-967
- **ZDI-CAN:** ZDI-CAN-10496
- **Date:** 2020-08-10
- **CVE:** CVE-2020-15639
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Marvell
- **Affected Products:** QConvergeConsole
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-967/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Marvell QConvergeConsole. Authentication is not required to exploit this vulnerability. The specific flaw exists within the decryptFile method of the FlashValidatorServiceImpl class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Marvell has issued an update to correct this vulnerability. More details can be found at: https://www.marvell.com/content/dam/marvell/en/public-collateral/fibre-channel/marvell-fibre-channel-security-advisory-2020-07.pdf

## Disclosure Timeline

- 2020-04-01 - Vulnerability reported to vendor
- 2020-08-10 - Coordinated public release of advisory
