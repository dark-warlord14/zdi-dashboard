# ZDI-25-002: Trend Micro Apex One LogServer Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-002
- **ZDI-CAN:** ZDI-CAN-24609
- **Date:** 2025-01-08
- **CVE:** CVE-2024-52050
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Amol Dosanjh of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-002/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Trend Micro Common Client Log Service. By creating a symbolic link, an attacker can abuse the service to create arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0018217

## Disclosure Timeline

- 2024-06-28 - Vulnerability reported to vendor
- 2025-01-08 - Coordinated public release of advisory
- 2025-01-08 - Advisory Updated
