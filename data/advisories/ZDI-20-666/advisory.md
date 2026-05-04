# ZDI-20-666: (0Day) Microsoft Windows WLAN Connection Profile Missing Authentication Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-666
- **ZDI-CAN:** ZDI-CAN-10037
- **Date:** 2020-05-19
- **CVE:** N/A
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-666/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of WLAN connection profiles. By creating a malicious profile, an attacker can disclose credentials for the machine account. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of an administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 01/21/20 – ZDI reported the vulnerability to the vendor and the vendor acknowledged 01/23/20 – The vendor sent a MSRC case number 01/28/20 – The vendor sent a differently encrypted mail that appeared to be a blank mail – but was, in fact, a decline 04/29/20 – ZDI requested a status update 04/30/20 – The vendor sent the decrypted content of the 01/28/20 mail indicating: “Microsoft has decided that it will not be fixing this vulnerability in the current version and we are closing this case.” 04/30/20 – ZDI replied that we had missed the prior mail and asked if this is certain 05/11/20 – The vendor replied to confirm “this one is not intended for immediate servicing” -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it.

## Disclosure Timeline

- 2020-01-21 - Vulnerability reported to vendor
- 2020-05-19 - Coordinated public release of advisory
- 2020-07-20 - Advisory Updated
