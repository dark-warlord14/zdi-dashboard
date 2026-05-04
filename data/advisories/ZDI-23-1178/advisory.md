# ZDI-23-1178: (Pwn2Own) HP Color LaserJet Pro M479fdw msws Probe Message Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1178
- **ZDI-CAN:** ZDI-CAN-19586
- **Date:** 2023-08-24
- **CVE:** CVE-2023-27971
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** HP
- **Affected Products:** Color LaserJet Pro M479fdw
- **Credit:** Neodyme
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1178/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of HP Color LaserJet Pro M479fdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of Probe messages. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

HP has issued an update to correct this vulnerability. More details can be found at: https://support.hp.com/us-en/document/ish_7919962-7920003-16/hpsbpi03839

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2023-08-24 - Coordinated public release of advisory
