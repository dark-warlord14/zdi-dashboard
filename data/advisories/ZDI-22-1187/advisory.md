# ZDI-22-1187: (Pwn2Own) ConnMan received_data Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1187
- **ZDI-CAN:** ZDI-CAN-17448
- **Date:** 2022-09-08
- **CVE:** CVE-2022-32292
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** ConnMan
- **Affected Products:** ConnMan
- **Credit:** David BERARD and Vincent DEHORS from @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1187/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installation of ConnMan. Authentication is not required to exploit this vulnerability. The specific flaw exists within the received_data method. Crafted data in a HTTP response can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the ConnMan process. This vulnerability was demonstrated on a Tesla Model 3 during Pwn2Own 2022 Vancouver competition.

## Additional Details

ConnMan has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/network/connman/connman.git/commit/?id=d1a5ede5d255bde8ef707f8441b997563b9312bd

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-09-08 - Coordinated public release of advisory
