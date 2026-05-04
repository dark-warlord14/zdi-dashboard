# ZDI-22-547: (0Day) (Pwn2Own) Samsung Galaxy S21 Exposed Dangerous Method Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-547
- **ZDI-CAN:** ZDI-CAN-15917
- **Date:** 2022-04-05
- **CVE:** N/A
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:H/A:N
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S21
- **Credit:** Sam Thomas (@_s_n_t) of Pentest Ltd (@pentestltd)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-547/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of Samsung Galaxy S21 phones. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within Web Bridge WebView. The WebView exposes a JavaScript interface that allows the attacker to launch arbitrary apps. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 12/30/21 – ZDI reported the vulnerability to vendor 02/02/22 – The vendor requested technical clarification 02/10/22 – ZDI provided additional evidence 02/17/22 - The vendor advised that the issue does not meet the bar for security servicing 03/28/22 – ZDI notified the vendor of the intention to publish the case as 0-day advisory on 04/04/22 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-12-30 - Vulnerability reported to vendor
- 2022-04-05 - Coordinated public release of advisory
