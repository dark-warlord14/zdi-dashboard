# ZDI-23-1621: Trend Micro Apex One Local File Inclusion Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1621
- **ZDI-CAN:** ZDI-CAN-21460
- **Date:** 2023-11-14
- **CVE:** CVE-2023-47202
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** NT AUTHORITY\ANONYMOUS LOGON
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1621/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One web console. The issue results from passing an insecure path to a PHP include function. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of IUSR.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000295652

## Disclosure Timeline

- 2023-07-26 - Vulnerability reported to vendor
- 2023-11-14 - Coordinated public release of advisory
