# ZDI-23-094: Netatalk dsi_writeinit Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-094
- **ZDI-CAN:** ZDI-CAN-17646
- **Date:** 2023-02-06
- **CVE:** CVE-2022-43634
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Netatalk
- **Affected Products:** Netatalk
- **Credit:** Corentin BAYET (@OnlyTheDuck), Etienne HELLUY-LAFONT and Luca MORO (@johncool__) from Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-094/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Netatalk. Authentication is not required to exploit this vulnerability. The specific flaw exists within the dsi_writeinit function. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Netatalk has issued an update to correct this vulnerability. More details can be found at: https://github.com/Netatalk/Netatalk/pull/186

## Disclosure Timeline

- 2022-06-03 - Vulnerability reported to vendor
- 2023-02-06 - Coordinated public release of advisory
