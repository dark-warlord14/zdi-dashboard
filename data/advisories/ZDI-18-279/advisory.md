# ZDI-18-279: Intel Security True Key SecureExecute Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-279
- **ZDI-CAN:** ZDI-CAN-4882
- **Date:** 2018-04-09
- **CVE:** CVE-2018-6661
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Intel Security
- **Affected Products:** True Key
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-279/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Intel Security True Key. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the TrueKey service, which listens on TCP port 30000 by default. A crafted message to the SecureExecute method can trigger it to launch insecure binaries. An attacker can leverage this vulnerability to escalate privilege to SYSTEM.

## Additional Details

Intel Security has issued an update to correct this vulnerability. More details can be found at: http://service.mcafee.com/FAQDocument.aspx?&id=TS102801

## Disclosure Timeline

- 2017-06-14 - Vulnerability reported to vendor
- 2018-04-09 - Coordinated public release of advisory
- 2018-04-09 - Advisory Updated
