# ZDI-22-520: (Pwn2Own) NETGEAR R6700v3 Improper Certificate Validation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-520
- **ZDI-CAN:** ZDI-CAN-15797
- **Date:** 2022-03-23
- **CVE:** CVE-2022-27644
- **CVSS:** 5.0
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700v3
- **Credit:** Kevin Denis (@0xmitsurugi) and Antide Petit (@xarkes_) from @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-520/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to compromise the integrity of downloaded information on affected installations of NETGEAR R6700v3 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the downloading of files via HTTPS. The issue results from the lack of proper validation of the certificate presented by the server. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064721/Security-Advisory-for-Multiple-Vulnerabilities-on-Multiple-Products-PSV-2021-0324

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
