# ZDI-24-1082: (0Day) (Pwn2Own) oFono AT CMGR Command Uninitialized Variable Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1082
- **ZDI-CAN:** ZDI-CAN-23309
- **Date:** 2025-12-10
- **CVE:** CVE-2024-7542
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** oFono
- **Affected Products:** oFono
- **Credit:** Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1082/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of oFono. An attacker must first obtain the ability to execute code on the target modem in order to exploit this vulnerability. The specific flaw exists within the parsing of responses from AT+CMGR commands. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Update as of 12/10/2025: These were addressed here https://lore.kernel.org/ofono/20241217093207.20636-2-absicsz@gmail.com/ 08/05/24 – ZDI made multiple attempts to report the vulnerability to the vendor via the oFono distribution list, Red Hat, and upstream Linux Kernel, but the vendor did not respond. The Linux Kernel informed ZDI that since it “has nothing to do with the Linux Kernel,” we should report it to the distribution list. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-02-29 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
