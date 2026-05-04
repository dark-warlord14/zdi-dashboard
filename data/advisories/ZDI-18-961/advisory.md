# ZDI-18-961: Trend Micro Maximum Security ID_AMSP_MASTER Deserialization of Untrusted Data Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-961
- **ZDI-CAN:** ZDI-CAN-6102
- **Date:** 2018-08-30
- **CVE:** CVE-2018-10513
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Maximum Security
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-961/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Trend Micro Maximum Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within processing of ID_AMSP_MASTER requests in the service process coreServiceShell.exe. When parsing the request buffer, the process does not properly validate user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://esupport.trendmicro.com/en-US/home/pages/technical-support/1120742.aspx

## Disclosure Timeline

- 2018-04-19 - Vulnerability reported to vendor
- 2018-08-30 - Coordinated public release of advisory
- 2018-08-30 - Advisory Updated
