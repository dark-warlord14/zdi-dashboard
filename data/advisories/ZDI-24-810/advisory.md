# ZDI-24-810: Hewlett Packard Enterprise OneView startUpgradeCommon Command Injection Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-810
- **ZDI-CAN:** ZDI-CAN-22454
- **Date:** 2024-06-18
- **CVE:** CVE-2023-50274
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** OneView
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-810/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges code on affected installations of Hewlett Packard Enterprise OneView. An attacker must first obtain the ability to execute low-privileged code on the target system or send an HTTP request to a local service in order to exploit this vulnerability. The specific flaw exists within the startUpgradeCommon method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbgn04586en_us&docLocale=en_US

## Disclosure Timeline

- 2023-12-01 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
