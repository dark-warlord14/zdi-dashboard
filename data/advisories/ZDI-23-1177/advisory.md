# ZDI-23-1177: (Pwn2Own) HP Color LaserJet Pro M479fdw slangapp PATH_INFO Stack-based Buffer Overflow Remote Code Execution

## Metadata

- **ZDI ID:** ZDI-23-1177
- **ZDI-CAN:** ZDI-CAN-19765
- **Date:** 2023-08-24
- **CVE:** CVE-2023-35178
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** HP
- **Affected Products:** Color LaserJet Pro M479fdw
- **Credit:** Bugscale
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1177/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of HP Color LaserJet Pro M479fdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the slangapp binary. When parsing the value of the passed PATH_INFO variable, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

HP has issued an update to correct this vulnerability. More details can be found at: https://support.hp.com/us-en/document/ish_8651729-8651769-16/hpsbpi03854

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2023-08-24 - Coordinated public release of advisory
