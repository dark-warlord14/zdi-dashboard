# ZDI-06-019: GraceNote CDDBControl ActiveX Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-019
- **ZDI-CAN:** ZDI-CAN-040
- **Date:** 2006-06-27
- **CVE:** CVE-2006-3134
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** GraceNote
- **Affected Products:** ActiveX CDDB Control
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-019/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems that have some versions of the GraceNote CDDBControl ActiveX object installed. There is a buffer overflow in an ActiveXObject registered by several products that use the Gracenote CDDB for CD information lookup. The ActiveX Object is commonly registered as safe and can be accessed from a malicious web site. The specific flaw exists when a large string is supplied as an option for the instantiated control. An attacker can gain control of the process leading to arbitrary code execution.

## Additional Details

Recently, a security vulnerability was found within a limited number of our products. This is the first time we have been made aware of any security vulnerability, and to date we have not received any reports of end users being affected by this issue. As soon as this vulnerability was detected Gracenote took immediate action and followed every required step to address this matter. As a solution, we have developed a software patch which is being provided to all of our affected customers and they will be working through their normal channels and processes to alert end-users and to update and fix affected applications.

## Disclosure Timeline

- 2006-04-17 - Vulnerability reported to vendor
- 2006-06-27 - Coordinated public release of advisory
