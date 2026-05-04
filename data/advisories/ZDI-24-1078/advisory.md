# ZDI-24-1078: (0Day) (Pwn2Own) oFono CUSD AT Command Stack-based Buffer Overflow Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1078
- **ZDI-CAN:** ZDI-CAN-23190
- **Date:** 2024-08-05
- **CVE:** CVE-2024-7538
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** oFono
- **Affected Products:** oFono
- **Credit:** Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1078/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of oFono. An attacker must first obtain the ability to execute code on the target modem in order to exploit this vulnerability. The specific flaw exists within the parsing of responses from AT Commands. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Update as of 12/10/2025: This is fixed here https://lore.kernel.org/ofono/20241217093207.20636-3-absicsz@gmail.com/ 08/05/24 – ZDI made multiple attempts to report the vulnerability to the vendor via the oFono distribution list, Red Hat, and upstream Linux Kernel, but the vendor did not respond. The Linux Kernel informed ZDI that since it “has nothing to do with the Linux Kernel,” we should report it to the distribution list. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-08-05 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
