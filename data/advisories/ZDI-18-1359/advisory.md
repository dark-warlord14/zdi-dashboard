# ZDI-18-1359: Epic Games Launcher Protocol Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1359
- **ZDI-CAN:** ZDI-CAN-7241
- **Date:** 2018-11-23
- **CVE:** CVE-2018-17707
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Epic Games
- **Affected Products:** Epic Games Launcher
- **Credit:** rgod of 9sg Security Team - rgod@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1359/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Visual Studio with tools for Unreal Engine development installed. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handler for the com.epicgames.launcher protocol. A crafted URI with the com.epicgames.launcher protocol can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Fixed in version 8.2.2

## Disclosure Timeline

- 2018-09-14 - Vulnerability reported to vendor
- 2018-11-23 - Coordinated public release of advisory
