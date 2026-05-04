# ZDI-22-621: (Pwn2Own) Samsung Galaxy S21 loadUrl Open Redirect Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-621
- **ZDI-CAN:** ZDI-CAN-15918
- **Date:** 2022-04-12
- **CVE:** CVE-2022-1230
- **CVSS:** 3.9
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S21
- **Credit:** Sam Thomas (@_s_n_t) of Pentest Ltd (@pentestltd)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-621/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of Samsung Galaxy S21 phones. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of redirections. An attacker can force a redirection to a site that serves malicious content. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the current user.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/serviceWeb.smsb

## Disclosure Timeline

- 2021-12-30 - Vulnerability reported to vendor
- 2022-04-12 - Coordinated public release of advisory
