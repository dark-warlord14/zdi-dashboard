# ZDI-20-1226: Trend Micro OfficeScan Hard Link Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1226
- **ZDI-CAN:** ZDI-CAN-10794
- **Date:** 2020-09-25
- **CVE:** CVE-2020-24562
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** OfficeScan
- **Credit:** Tran Van Khang - khangkito of VinCSS (Member of Vingroup)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1226/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro OfficeScan. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the OfficeScan Security Agent. By creating a hard link, an attacker can abuse the service to overwrite the contents of a chosen file. An attacker can leverage this vulnerability to escalate privileges and execute code as an administrator.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000263633

## Disclosure Timeline

- 2020-05-29 - Vulnerability reported to vendor
- 2020-09-25 - Coordinated public release of advisory
