# ZDI-10-128: Ipswitch Imail Server Queuemgr Format String Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-128
- **ZDI-CAN:** ZDI-CAN-738
- **Date:** 2010-07-15
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Ipswitch
- **Affected Products:** IMail
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-128/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IPSwitch IMail. Authentication is not required to exploit this vulnerability. The specific flaw exists within SMTPDLL.dll (called by queuemgr.exe). When handling a message queued for remote delivery user supplied data can be used to specify additional format specifiers to a vsprintf call. This can be accomplished by providing a specially crafted -NOTIFY argument to the SMTP "RCPT TO:" argument. Additionally, the destination buffer supplied to vsprintf is a local stack buffer and can also be overflowed with a large -NOTIFY argument. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Update to the latest version 11.02

## Disclosure Timeline

- 2010-06-08 - Vulnerability reported to vendor
- 2010-07-15 - Coordinated public release of advisory
