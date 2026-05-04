# ZDI-18-962: Trend Micro Maximum Security ID_AMSP_MASTER Missing Impersonation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-962
- **ZDI-CAN:** ZDI-CAN-6103
- **Date:** 2018-08-30
- **CVE:** CVE-2018-10514
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-962/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within processing of request ID 0x2ff0000b in request ID_AMSP_MASTER by the coreServiceShell service. The service does not properly impersonate the client before executing sensitive operations. An attacker can leverage this vulnerability to escalate privileges to SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://esupport.trendmicro.com/en-US/home/pages/technical-support/1120742.aspx

## Disclosure Timeline

- 2018-04-19 - Vulnerability reported to vendor
- 2018-08-30 - Coordinated public release of advisory
- 2018-08-30 - Advisory Updated
