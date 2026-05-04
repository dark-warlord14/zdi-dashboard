# ZDI-22-1175: Trend Micro Maximum Security Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1175
- **ZDI-CAN:** ZDI-CAN-14557
- **Date:** 2022-08-31
- **CVE:** CVE-2022-34893
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** brsn (@brsn76945860)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1175/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Trend Micro Anti-Malware Solution Platform. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-11053

## Disclosure Timeline

- 2022-03-02 - Vulnerability reported to vendor
- 2022-08-31 - Coordinated public release of advisory
