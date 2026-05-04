# ZDI-25-1069: (Pwn2Own) oFono CUSD Stack-based Buffer Overflow Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1069
- **ZDI-CAN:** ZDI-CAN-23193
- **Date:** 2025-12-10
- **CVE:** CVE-2024-7539
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** oFono
- **Affected Products:** oFono
- **Credit:** Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1069/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of oFono. An attacker must first obtain the ability to execute code on the target modem in order to exploit this vulnerability. The specific flaw exists within the parsing of responses from AT+CUSD commands. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

oFono has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/ofono/20241217093207.20636-3-absicsz@gmail.com/

## Disclosure Timeline

- 2024-02-29 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
