# ZDI-24-560: Lexmark CX331adwe Firmware Downgrade Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-560
- **ZDI-CAN:** ZDI-CAN-22550
- **Date:** 2024-05-31
- **CVE:** CVE-2023-50738
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Lexmark
- **Affected Products:** CX331adwe
- **Credit:** Foundry Zero
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-560/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark CX331adwe printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the `/usr/bin/hydra` service, which listens on TCP port 9100 by default. The issue results from the lack of proper validation of a firmware image before using it to perform an upgrade. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://www.lexmark.com/en_us/solutions/security/lexmark-security-advisories.html

## Disclosure Timeline

- 2023-12-01 - Vulnerability reported to vendor
- 2024-05-31 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
