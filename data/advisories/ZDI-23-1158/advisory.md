# ZDI-23-1158: McAfee Safe Connect VPN Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1158
- **ZDI-CAN:** ZDI-CAN-20770
- **Date:** 2023-08-21
- **CVE:** CVE-2023-40352
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** McAfee
- **Affected Products:** Safe Connect VPN
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1158/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of McAfee Safe Connect VPN. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The product loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

McAfee has issued an update to correct this vulnerability. More details can be found at: https://www.mcafee.com/support/?articleId=TS103462&page=shell&shell=article-view

## Disclosure Timeline

- 2023-04-28 - Vulnerability reported to vendor
- 2023-08-21 - Coordinated public release of advisory
