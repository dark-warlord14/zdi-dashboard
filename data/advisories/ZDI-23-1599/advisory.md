# ZDI-23-1599: Hewlett Packard Enterprise OneView Backup Hard-coded Cryptographic Key Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1599
- **ZDI-CAN:** ZDI-CAN-21806
- **Date:** 2023-11-14
- **CVE:** CVE-2023-30912
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** OneView
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1599/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hewlett Packard Enterprise OneView. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the Backup functionality. The issue results from the product's use of a hard-coded cryptographic key. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=hpesbgn04548en_us

## Disclosure Timeline

- 2023-07-26 - Vulnerability reported to vendor
- 2023-11-14 - Coordinated public release of advisory
