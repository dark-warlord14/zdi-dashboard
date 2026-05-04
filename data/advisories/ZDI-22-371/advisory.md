# ZDI-22-371: Trend Micro Antivirus for Mac Link Following Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-371
- **ZDI-CAN:** ZDI-CAN-14998
- **Date:** 2022-02-16
- **CVE:** CVE-2022-24671
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Antivirus for Mac
- **Credit:** Cees Elzinga
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-371/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Antivirus for Mac. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the program_after_update script. By creating a symbolic link, an attacker can abuse the product to loosen permissions on a local file. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-10937

## Disclosure Timeline

- 2021-10-15 - Vulnerability reported to vendor
- 2022-02-16 - Coordinated public release of advisory
